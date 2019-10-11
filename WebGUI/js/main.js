$(function(){
    $("#table-btn").click(function(){
        $("#login-modal").fadeIn();
    });

    $("#submit-btn").click(function(){
        $("#login-modal").fadeOut();
    });

    $("#camstream").attr('data', 'http://' + location.hostname + ':10000/stream?topic=/image');
    
    var ros = new ROSLIB.Ros({url: "ws://" + location.hostname + ":9000"});

    ros.on("connection", function(){console.log("websocket: connected");});
    ros.on("error", function(error){console.log("websocket error", error);});
    ros.on("close", function(){console.log("websocket: closed");});

    var ls = new ROSLIB.Topic({
        ros : ros,
        name : 'lightsensor_val',
        messageType : 'raspi_ros/LightSensors',
    })

    ls.subscribe(message => {
        $(".value-right-side-modal").text(message.r_side);
        $(".value-right-front-modal").text(message.r_front);
        $(".value-left-front-modal").text(message.l_front);
        $(".value-left-side-modal").text(message.l_side);
        $(".value-sum-all-modal").text(message.sum);
        $(".value-sum-front-modal").text(message.sum_forward);

        $(".value-right-side").text(message.r_side);
        $(".value-right-front").text(message.r_front);
        $(".value-left-front").text(message.l_front);
        $(".value-left-side").text(message.l_side);
        $(".value-sum-all").text(message.sum);
        $(".value-sum-front").text(message.sum_forward);
        
        //console.log(message);

        
    });
});