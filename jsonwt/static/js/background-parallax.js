/*
 * Based on Paraxify.js v0.1 library by Jaime Caballero, MIT license (https://github.com/jaicab/Paraxify.js)
 */

window.BackgroundParallax = (function (window, $) {
    'use strict';
    var self;

    /***
     * BackgroundParallax object
     *
     */
    function BackgroundParallax(config) {
        self = this;
        self.config = $.extend(self.defaults, config);

        self.$parallaxEls = null;
        self.screenHeight = 0;
        self.scrollY = 0;
        self.parallaxElsData = null;

        self.init();
    }


    BackgroundParallax.prototype = {

        defaults: {
            mobile: true,
            selector: '.fr-background-parallax-active',
            speed: 1,
            boost: 0
        },


        init: function () {
            if (self._isMobile() && !self.config.mobile) {
                $('body').addClass('isTouchDevice');

                self.destroy();
                return;
            }

            self.$parallaxEls = $(self.config.selector);

            if (!self.$parallaxEls.length) {
                return;
            }

            self.parallaxElsData = [];

            $(window).on('resize', self._updateParallax);
            $(window).on('scroll', self._updateBackgroundPosition);

            self._updateParallax();
        },


        destroy: function () {
            $(window).off('resize', self._updateParallax);
            $(window).off('scroll', self._updateBackgroundPosition);

            if (self.$parallaxEls) {
                self.$parallaxEls.each(function () {
                    $(this).removeAttr('style');
                });

                self.$parallaxEls = null;
            }

            self.parallaxElsData = null;
        },


        _updateParallax: function () {
            self.screenHeight = window.innerHeight;
            self.scrollY = window.pageYOffset;

            self.$parallaxEls.each(function (i) {
                var $el = $(this);
                self.parallaxElsData[i] = {};

                $el.css('background-position', 'center center');

                var bgImg = $el.css('background-image');
                var bgImgUrl = bgImg.match(/url\((['"])?(.*?)\1\)/i);
                if (bgImgUrl) {
                    bgImgUrl = bgImgUrl[2];
                }

                self.parallaxElsData[i].hasOverlayColor = bgImg.indexOf('linear-gradient(') !== -1;
                self.parallaxElsData[i].url = bgImgUrl;
                self.parallaxElsData[i].img = self.parallaxElsData[i].img || new Image();

                self._readBackgroundImageDimensions(i);
                if (bgImgUrl !== self.parallaxElsData[i].img.src) {
                    self.parallaxElsData[i].img.src = bgImgUrl;
                }

            });

            self._updateBackgroundPosition();
        },


        _readBackgroundImageDimensions: function (i) {
            var $el = $(self.$parallaxEls[i]);

            self.parallaxElsData[i].ok = true;
            self.parallaxElsData[i].bgSize = $el.css('background-size');

            var actualHeight = self.screenHeight;
            var speedAttr = $el.attr('data-fr-background-parallax-speed');

            // Speed in data attribute is saved in range -100 to +100
            // meaning when less than 0 background is moving slower than scroll
            // and when more than 0 background is moving faster than scroll.
            // Here we convert it to range 0 to 2.
            if (speedAttr) {
                if (speedAttr > 0) {
                    speedAttr = speedAttr / 100 + 1;
                }
                else if (speedAttr < 0) {
                    speedAttr = speedAttr / -100;
                }
            }
            var speed = speedAttr || self.config.speed;

            // set parallax speed to same value as speed to get more expressive parralax effect
            var boost = speed;

            self.parallaxElsData[i].img.onload = self.parallaxElsData[i].img.onload || function () {
                if (!self.parallaxElsData[i].img.complete) {
                    return;
                }

                if (self.screenHeight < $el.outerHeight()) {
                    self.parallaxElsData[i].ok = false;
                    console.warn("The container (" + $el.outerHeight() + "px) can't be bigger than the image (" + self.screenHeight + "px).");
                }

                self.parallaxElsData[i].onloadFired = true;

                self._updateParallaxElDiff(i, $el, actualHeight, speed, boost);
                self._updateBackgroundPositionOf(i);
            };

            // HTMLImageElement.complete
            // Returns a Boolean that is true if the browser has fetched the image,
            // and it is in a supported image type that was decoded without errors.
            if (self.parallaxElsData[i].img.complete) {
                if (self.parallaxElsData[i].onloadFired) {
                    self._updateParallaxElDiff(i, $el, actualHeight, speed, boost);
                }
                else {
                    self.parallaxElsData[i].img.onload();
                }
            }
        },


        _updateParallaxElDiff: function (i, $el, actualHeight, speed, boost) {
            var diff = -(actualHeight - $el.outerHeight()) * speed;
            diff -= ($el.outerHeight() * boost);

            self.parallaxElsData[i].diff = diff;
        },


        _isElementInViewport: function (i) {
            var el = self.$parallaxEls[i];
            var rect = el.getBoundingClientRect();

            return (
                // top edge is inside viewport
            (rect.top >= 0 && rect.top < (window.innerHeight || document.documentElement.clientHeight)) ||
                // bottom edge is inside viewport
            (rect.bottom > 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight)) ||
                // both top and bottom edges are outside viewport (element higher than viewport)
            (rect.top <= 0 && rect.bottom >= (window.innerHeight || document.documentElement.clientHeight))
            );
        },


        _updateBackgroundPosition: function () {
            self.scrollY = window.pageYOffset;

            self.$parallaxEls.each(function (i) {
                self._updateBackgroundPositionOf(i);
            });
        },


        _updateBackgroundPositionOf: function(i) {
            var per, position;

            var $el = $(self.$parallaxEls[i]);
            if (self.parallaxElsData[i].ok && self._isElementInViewport(i)) {
                per = (self.scrollY - $el.offset().top + self.screenHeight) / ($el.outerHeight() + self.screenHeight);
                position = self.parallaxElsData[i].diff * (per - 0.5);
                position = (Math.round(position * 100) / 100) + 'px';
            }
            else {
                position = 'center';
            }

            // update css if position has changed
            if (self.parallaxElsData[i].position !== position) {
                self.parallaxElsData[i].position = position;
                // Overlay color (linear-gradient) is element size therefore shouldn't be moved
                if (self.parallaxElsData[i].hasOverlayColor) {
                    $el.css('background-position', '0 0, center ' + position);
                }
                else {
                    $el.css('background-position', 'center ' + position);
                }
            }
        },


        _isMobile: function () {
            var agent = navigator.userAgent || navigator.vendor || window.opera;

            return (/(ipad|playbook|silk|android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(agent) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(agent.substr(0, 4))) ? true : false;
        },


        _injectElementWithStyles: function (rule, callback, nodes, testnames) {

            var style, ret, node, docOverflow,
                div = document.createElement('div'),
                body = document.body,
                fakeBody = body || document.createElement('body'),
                mod = 'modernizr';

            if (parseInt(nodes, 10)) {
                while (nodes--) {
                    node = document.createElement('div');
                    node.id = testnames ? testnames[nodes] : mod + (nodes + 1);
                    div.appendChild(node);
                }
            }

            style = ['&#173;', '<style id="s', mod, '">', rule, '</style>'].join('');
            div.id = mod;
            (body ? div : fakeBody).innerHTML += style;
            fakeBody.appendChild(div);
            if (!body) {
                fakeBody.style.background = '';
                fakeBody.style.overflow = 'hidden';
                docOverflow = docElement.style.overflow;
                docElement.style.overflow = 'hidden';
                docElement.appendChild(fakeBody);
            }

            ret = callback(div, rule);
            if (!body) {
                fakeBody.parentNode.removeChild(fakeBody);
                docElement.style.overflow = docOverflow;
            } else {
                div.parentNode.removeChild(div);
            }

            return !!ret;
        }

    };

    return BackgroundParallax;

})(window, $);
