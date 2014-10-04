;(function($) {
    'use strict';
    var $body = $('html, body');
    var contentDiv = $('#content');
    var contentPosition = $('#content').position();

    var content = contentDiv.smoothState({
        prefetch: true,
        pageCacheSize: 4,
        onStart: {
            duration: 500,
            render: function (url, $container) {
                content.toggleAnimationClass('is-exiting');
                $body.animate({ scrollTop: contentPosition.top }, 500);
            }
        }
    }).data('smoothState');
})(jQuery);