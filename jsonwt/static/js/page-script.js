$(function () {
    'use strict';

    // creates widget animations
    if (window.RevealAnimation) {
        window.revealAnimation = new RevealAnimation();
    }

    // creates background parallax
    if (window.BackgroundParallax) {
        window.backgroundParallax = new BackgroundParallax();
    }

    // create slideshows
    var $slideshows = $('.swiper-container');
    if ($slideshows.length) {
        $slideshows.each(function () {
            var $slideshow = $(this),
                $slides = $slideshow.children('.fr-widget.fr-container'),
                $slideWraper = $slideshow.children('.swiper-wrapper');

            if ($slides.length && $slideWraper.length === 1) {
                $slides.addClass('swiper-slide');
                $slideWraper.append($slides);

                var swipperOptions = {
                    mode: 'horizontal',
                    loop: true,
                    speed: 1000
                };

                /* if autoplay is enabled, set autoplay interval */
                var autoplay = $slideshow.data('slideshowAutoplay');
                if (autoplay) {
                    swipperOptions['autoplay'] = autoplay;
                }

                /* if need to show dots, set the pagination container */
                if ($slideshow.data('slideshowDots')) {
                    swipperOptions['pagination'] = $slideshow.children('.fr-slideshow-dots')[0];
                    swipperOptions['paginationClickable'] = true;
                }

                /* generate the Swiper */
                var swiper = $slideshow.swiper(swipperOptions);

                /* add arrow button functionality to Swiper */
                var $arrows = $slideshow.children('.fr-widget.fr-img, .fr-widget.fr-svg'),
                    $arrowLeft = $arrows.eq(0),
                    $arrorRigt = $arrows.eq(1);

                if ($arrowLeft.length) {
                    $arrowLeft.on('click', function () {
                        swiper.swipePrev();
                    });
                }
                if ($arrorRigt.length) {
                    $arrorRigt.on('click', function () {
                        swiper.swipeNext();
                    });
                }
            }
        });
    }

    // used for navigation widget
    if (window.responsiveNav && $('.fr-navigation-active').length) {
        $('.fr-navigation').each(function () {
            var $navHeader = $(this);
            var $nav = $navHeader.children('.fr-container');
            var $navToggle = $navHeader.children('.fr-svg');
            window.navigation = window.responsiveNav($nav.attr('id'), {
                customToggle: $navToggle.attr('id'),
                closeOnNavClick: true,
                jsClass: 'x-nav-js',
                navClass: 'x-nav-collapse',
                navActiveClass: 'x-js-nav-active'
            });
        });
    }

    // anchor smooth scrolling
    $('a').click(function () {
        var href = this.href;

        if (!href || href.indexOf('#') === -1) {
            return;
        }

        var baseUrl = document.location.href.replace(document.location.hash, '');
        var isSameDocument = href.replace(baseUrl, '').indexOf('#') === 0;

        if (!isSameDocument) {
            return;
        }
        var hash = this.hash;
        var $element = $(hash);
        if (!$element.length) {
            return;
        }

        $('html,body').animate({
            scrollTop: $element.offset().top
        }, 500, function () {
            window.location.hash = hash;
        });
        return false;
    });

});
