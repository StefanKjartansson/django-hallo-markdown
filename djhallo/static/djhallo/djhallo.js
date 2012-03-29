(function ($) {
    "use strict";
    var converter = new Showdown.converter();
    var markdownize = function(content) {
        return toMarkdown(content.split("\n").map($.trim).filter(
            function(line) { return line !== ""; }).join("\n"));
    };
    var htmlize = function(content) {
        return converter.makeHtml(content);
    };

    $(function(){
        $('.hallo-block').each(function(idxx, i) {
            var edit = $(i).find('.edit'),
                source = $(i).find('textarea');
            $(edit).hallo({
                plugins: {
                    'halloformat': {},
                    'halloblock': {},
                    'hallolists': {},
                    'halloreundo': {}
                }
            });
            var showSource = function(content) {
                var markdown = markdownize(content);
                if ($(source).get(0).value === markdown) { return; }
                $(source).get(0).value = markdown;
            };
            var updateHtml = function(content) {
                if (markdownize($(edit).html()) === content) { return; }
                $(edit).html(htmlize(content));
            };
            $(edit).bind('hallomodified', function(event, data) {
                showSource(data.content);
            });
            $(source).bind('keyup', function() {
                updateHtml(this.value);
            });
            updateHtml($(source).val());
            return;
        });
    });
})(djhallo.jQuery);
