(function ($) {
    'use strict';

    $(function () {
        $('.fr-linktype-submit').click(function (e) {
            e.preventDefault();

            var $this = $(this);
            var $closestForm = $this.closest('form');
            if ($closestForm) {
                $closestForm.submit();
            }
        });
    });
})(window.jQuery);
