$(function(){
    $("#table-btn").click(function(){
        $("#login-modal").fadeIn();
    });

    $("#submit-btn").click(function(){
        $("#login-modal").fadeOut();
    });

    //$("#camstream").attr('data', 'http://' + location.hostname + ':10000/stream?topic=/cv_camera/image_raw');
    $("#camstream").attr('data', 'http://' + location.hostname + ':10000/stream?topic=/image');
    /*
    var ros = new ROSLIB.Ros({url: "ws://" + location.hostname + "9000"});

    ros.on("connection", function(){console.log("websocket: connected");});
    ros.on("error", function(error){console.log("websocket error", error);});
    ros.on("close", function(){console.log("websocket: closed");});

    */
});