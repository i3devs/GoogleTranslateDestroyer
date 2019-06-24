function validateForm() {

    let inputText = $("#input").val();

    if (inputText.length === 0) {
        alert("Please insert some text to destroy.");
        return false;
    }

    if (inputText.match("/^[a-z &0-9,.\\-!?àèìòùäëïöüÿ\"'çß]/gi")) {
        alert("The inserted text contains invalid characters.");
        return false;
    }

    const LANGS = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh", "co", "hr",
        "cs", "da", "nl", "en", "eo", "et", "fil", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha",
        "he", "hi", "hu", "is", "ig", "id", "ga", "it", "ja", "jv", "kn", "kk", "km", "ko", "ku", "ky", "lo",
        "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ps", "fa",
        "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su",
        "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu"];

    if (!LANGS.includes($("#init_lang").val().trim())) {

        alert("The selected language is invalid.");
        return false;

    }

    let langsNum = parseInt($("#langs_num").val().trim());
    if (isNaN(langsNum) || langsNum < 1 || langsNum > 99) {

        alert("The number of languages must be a valid integer number within the following interval:\n[1, 99]");
        return false;
    }

    return true;

}

// $("form").submit(function (evt) {
//
//     evt.preventDefault();
//
//     if (validateForm()) {
//
//         let langsNum = $("#langs_num").val();
//         let pageFade = $(".pageFade");
//
//         pageFade.show();
//
//         let bar = $("#myBar");
//         bar.animate({width: '100%'}, {
//             duration: langsNum * 1.8 * 1000, progress: function () {
//                 let width = bar.width();
//                 let parentWidth = bar.offsetParent().width();
//                 let percent = Math.floor(100 * width / parentWidth);
//                 bar.text(percent + "%");
//             }
//         });
//
//         $.post("./destroy", {
//             input: $("#input").val(),
//             languages_number: langsNum,
//             initial_language: $("#init_lang").val(),
//             csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
//         }, function (status) {
//             bar.width(bar.offsetParent().width());
//             pageFade.hide(); // To Hide progress bar
//             document.open();
//             document.write(status);
//             document.close();
//         });
//
//     }
//
// });
