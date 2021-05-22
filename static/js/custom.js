jQuery(function ($) {
    $(document).on('keypress', '[data-toggle="form2json"] input', function (event) {
        // enter pressionado?
        if (event.which == 13) {
            // busca o form a quem ele pertence
            $(event.target.form).trigger('submit');
        }
    });

    // dispara o submit indiretamente
    $(document).on('click', '[data-form2json="submit"]', function (event) {
        $(event.target.form).trigger('submit');
    });
});
