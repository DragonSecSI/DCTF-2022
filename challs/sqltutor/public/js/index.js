$(document)
.on("ready", function () {
  $("hi").on("click", function () {
    $(this).addClass("blue");
  });
});
