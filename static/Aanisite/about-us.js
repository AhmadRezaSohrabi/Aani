$(document).ready(function () {
  
    $('div.about-us-titles div').css('display', 'none').slideDown(2000)
    $('#history').click(function () {
        $("#historyText").fadeIn(1000);
        $("#viewText").css("display", "none");
        $("#missionText").css("display", "none");
        $("#holdingGroupText").css("display", "none");
        $("#eventText").css("display", "none");
    });
    $('#view').click(function () {
        $("#viewText").fadeIn(1000);
        $("#historyText").css("display", "none");
        $("#missionText").css("display", "none");
        $("#holdingGroupText").css("display", "none");
        $("#eventText").css("display", "none");
    });
    $('#mission').click(function () {
        $("#missionText").fadeIn(1000);
        $("#historyText").css("display", "none");
        $("#viewText").css("display", "none");
        $("#holdingGroupText").css("display", "none");
        $("#eventText").css("display", "none");
    });
    $('#holdingGroup').click(function () {
        $("#holdingGroupText").fadeIn(1000);
        $("#historyText").css("display", "none");
        $("#missionText").css("display", "none");
        $("#viewText").css("display", "none");
        $("#eventText").css("display", "none");
    });
    $('#events').click(function () {
        $("#eventText").fadeIn(1000);
        $("#historyText").css("display", "none");
        $("#missionText").css("display", "none");
        $("#holdingGroupText").css("display", "none");
        $("#viewText").css("display", "none");
    });

    $('#about-us-tag').click(function () {
        $("#historyText").css("display", "none");
        $("#missionText").css("display", "none");
        $("#viewText").css("display", "none");
        $("#eventText").css("display", "none");
        $("#holdingGroupText").css("display", "none");
    });
})