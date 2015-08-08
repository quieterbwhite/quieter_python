window.RevealAnimation = (function (window, Waypoint, $) {
    'use strict';

    var self,

        /**
         * RequestAnimationFrame polyfill.
         */
        _requestAnimFrame = (function () {

            return window.requestAnimationFrame ||
                window.webkitRequestAnimationFrame ||
                window.mozRequestAnimationFrame ||

                function (callback) {
                    window.setTimeout(callback, 1000 / 60);
                };
        }(window)),

        /**
         * CancelAnimationFrame polyfill.
         */
        _cancelAnimationFrame = (function () {

            return window.cancelAnimationFrame ||
                window.webkitCancelAnimationFrame ||
                window.webkitCancelRequestAnimationFrame ||
                window.mozCancelAnimationFrame ||
                window.mozCancelRequestAnimationFrame ||

                function (id) {
                    clearTimeout(id);
                };
        }(window));


    /**
     * Reveal Animation object, ensures that animations plays nice
     *
     * @param {Object} config - configuration for reveal Animation
     * @param {boolean} [config.mobile = true] - Weather to run animations on mobile devices.
     * @param {boolean} [config.repeat = true] - Weather to repeat the animations on subsequent reveals.
     * @param {string} [config.resultClass = 'fr-anim-result'] - Animation end state class name.
     * @param {string} [config.classPrefix = 'fr-anim'] - Prefix to use for animation classes extracted from
     *                                                    data attribute. Resulting class name will be
     *                                                    config.classPrefix + class in data attribute.
     * @param {string} [config.animationMarker = '.fr-having-animation'] - jQuery selector for elements to animate.
     * @param {string} [config.animationDataAttr = 'fr-animation'] = data attribute witch contains animation classes.
     */
    function RevealAnimation(config) {
        self = this;
        self.animations = {};
        self.elements = [];
        self.index = 1;
        self.initialConfig = self.config = $.extend({}, self.defaults, config);

        if (self._isMobile() && !self.config.mobile || !self._isSupported()) {
            self.destroy();
            return;
        }

        // Safari/OSX needs some additional time to get correct element locations.
        setTimeout(function() {
            self.init();
        }, 100);
    }

    RevealAnimation.prototype = {

        defaults: {
            mobile: true,
            repeat: true,
            resultClass: 'fr-anim-result',  // resets the state of animation class causing animation
            classPrefix: 'fr-anim',  // prefix to use for animation classes extracted from data attribute
            animationMarker: '.fr-having-animation',  // jQuery selector
            animationDataAttr: 'fr-animation'  // data attribute which contains animation classes: 'data-' + animationDataAttr
        },


        /**
         * Queries the DOM, builds animations.
         * @param {Object} config - Configuration options that will override the instance configuration.
         *                          For option keys see constructor.
         */
        init: function (config) {
            var index, animation,
                $elems = $(self.config.animationMarker);

            // Override config with passed object, if any
            self.config = $.extend({}, self.initialConfig, config);

            $.each($elems, function (i, el) {
                if (self.elements.indexOf(el) === -1) {
                    index = self.index++;
                    animation = self.animations[index] = {element: el};
                    animation.animationFrame = null;

                    // if animations need to be repeated, create animation reset waypoint
                    // to avoid the flicker of elements
                    if (self.config.repeat) {
                        animation.reset = self._createResetWaypoint(el);

                    } else {
                        animation.reset = null;
                    }
                    self.elements.push(el);

                    // if this element is already in elems object,
                    // destroy it's waypoint and recreate it to play the new animation if in view
                } else {
                    animation = self._getAnimationByElement(el);

                    if (animation.waypoint) {
                        animation.waypoint.destroy();
                    }
                    self._stopRuningAnimation(animation);
                }
                animation.animationClass = self._createAnimationClass(el);
                animation.waypoint = self._createWaypoint(el);
                animation.seen = false;
            });
        },


        /**
         * animates element using animation
         *
         * @param {Object} animation - animation Object from self.animations
         */
        animate: function (animation) {
            if (!animation || animation.seen || !animation.animationClass) {
                return false;
            }
            var $el = $(animation.element);

            // if animation is playing, stop it
            self._stopRuningAnimation(animation);

            // removeing resulting state, if it's there
            $el.removeClass(self.config.resultClass);

            // adding initial state, if it's not added already
            $el.addClass(animation.animationClass);

            // reqiuesting animation frame for animation to happen
            animation.animationFrame = _requestAnimFrame(function () {
                // adding resulting state and doing animation
                $el.addClass(self.config.resultClass);

                // when transition ends remove all animation classes
                $el.on('transitionend webkitTransitionEnd oTransitionEnd otransitionend MSTransitionEnd', function (e) {
                    if ($el.is(e.target)) {
                        // after css animation is done remove animation classes
                        $el.removeClass(self.config.resultClass + ' ' + animation.animationClass);
                        animation.animationFrame = null;
                        $el.off('transitionend webkitTransitionEnd oTransitionEnd otransitionend MSTransitionEnd');
                    }
                });
            });
            animation.seen = true;

            return true;
        },


        /**
         * destroys this object and clears the memory
         */
        destroy: function () {
            if (!self.animations) {
                return;
            }

            for (var i in self.animations) {

                if (self.animations.hasOwnProperty(i)) {
                    var animation = self.animations[i];

                    if (animation.waypoint) {
                        animation.waypoint.destroy();
                    }
                    if (animation.reset) {
                        animation.reset.destroy();
                    }

                    var $el = $(animation.element);
                    $el.removeClass(animation.animationClass);
                }
            }

            self.waypoints = null;
            self.elements = [];
            self.animations = {};
        },

        /**
         * Checks weather this is a mobile browser
         */
        _isMobile: function () {
            var agent = navigator.userAgent || navigator.vendor || window.opera;

            return (/(ipad|playbook|silk|android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(agent) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(agent.substr(0, 4))) ? true : false;
        },

        /**
         * Checks weather CSS Transitions are supported by browser
         */
        _isSupported: function () {
            var sensor = document.createElement('sensor'),
                cssPrefixTransition = [
                    'webkit',  /* Webkit understands both lower and upper case prefixes.
                                  Using lower because dumped objects return lower
                                  e.g. (console.log(document.body.style)) */
                    'Moz',  // FireFox understands only uppercase
                    'O',
                    'transition'],
                tests = (cssPrefixTransition.join('Transition,')).split(',');

            for (var i = 0; i < tests.length; i++) {

                if (tests[i] in sensor.style) {
                    return true;
                }
            }

            return false;
        },


        /**
         * creates and applies the animation class of the element
         * animation class is the base state of element
         *
         * @param {Element} element - DOM Element Node on witch the animation will be played
         */
        _createAnimationClass: function (element) {
            var animationString = element.getAttribute('data-' + self.config.animationDataAttr),
                animationClass = '';

            if (animationString) {
                var animations = animationString.split(' ');
                element.removeAttribute('data-' + self.config.animationDataAttr);

                animations.forEach(function (animation) {
                    animationClass += (' ' + self.config.classPrefix + '-' + animation);
                });
            }
            $(element).addClass(animationClass);

            return animationClass.trim();
        },


        /*
         * creates waypoint in witch the animation will be played
         *
         * @param {Element} element - DOM Element Node on witch the animation will be played
         */
        _createWaypoint: function (element) {
            return new Waypoint({
                element: element,
                handler: function (direction) {
                    var animation = self._getAnimationByElement(this.element);

                    // if scrolling down, play the animation
                    if (direction === 'down' && !animation.seen) {

                        if (!self.animate(animation) || !self.config.repeat) {
                            this.destroy();
                        }
                    }
                },
                offset: '90%'
            });
        },


        /**
         * Creates Waypoint that resets animation state for repeating
         *
         * @param {Element} element - DOM Element Node on witch the animation will be reset
         */
        _createResetWaypoint: function (element) {
            return new Waypoint({
                element: element,
                handler: function (direction) {

                    if (direction === 'up') {
                        var animation = self._getAnimationByElement(this.element);

                        if (animation.seen) {
                            self._stopRuningAnimation(animation);
                            $(this.element).addClass(animation.animationClass);
                            animation.seen = false;
                        }
                    }
                },
                offset: '100%'
            });
        },


        /**
         * returns animation element using dom element
         *
         * @param {Element} element - DOM Element Node
         */
        _getAnimationByElement: function (element) {
            for (var i in self.animations) {
                if (self.animations[i].element === element) {
                    return self.animations[i];
                }
            }

            return false;
        },


        /**
         * stops any executing animations on element using animation object
         * must pass animation from self.animations, not a dom element
         *
         * @param {Object} animation - animation Object from self.animations
         */
        _stopRuningAnimation: function (animation) {
            if (animation.animationFrame) {
                var $el = $(animation.element);

                $el.removeClass(self.config.resultClass + ' ' + animation.animationClass);
                $el.off('transitionend webkitTransitionEnd oTransitionEnd otransitionend MSTransitionEnd');
                _cancelAnimationFrame(animation);
                animation.animationFrame = null;
            }
        }
    };

    return RevealAnimation;

})(window, Waypoint, $);


