//var video = null;
setTimeout(function(){
	video = document.getElementById("video_src");

	$("#play-pause").click(function(){
		console.log("on")
		if (video.paused == true) {
			video.play();
			$("#video-controls").addClass("fade");
			$("#play-pause span").removeClass("glyphicon-play");
			$("#play-pause span").addClass("glyphicon-pause");
		} else {
			video.pause();
			$("#video-controls").removeClass("fade");
			$("#play-pause span").removeClass("glyphicon-pause");
			$("#play-pause span").addClass("glyphicon-play");
		}
	})

	$("#video_src").click(function(){
		if (video.paused == true) {
			video.play();
			$("#video-controls").addClass("fade");
			$("#play-pause span").removeClass("glyphicon-play");
			$("#play-pause span").addClass("glyphicon-pause");
		} else {
			video.pause();
			$("#video-controls").removeClass("fade");
			$("#play-pause span").removeClass("glyphicon-pause");
			$("#play-pause span").addClass("glyphicon-play");
		}
	})

	video.addEventListener("timeupdate", function() {
		var value = Math.round((100 / video.duration) * video.currentTime*100)/100;
		$("#seek-bar").attr("value",value);
		$("#seekthumb").css({left:(value/100 * (($("#seeklength").width())-15))});
		var time = video.currentTime;
		var dur = video.duration;
		$("#time").text(timeFormat(time,dur));
	});

	video.addEventListener("ended",function(){
		video.pause();
		$("#play-pause span").removeClass("glyphicon-pause");
		$("#play-pause span").addClass("glyphicon-play");
		video.currentTime = 0;
		$("#seek-bar").attr("value",0);
		$("#seekthumb").css({left:0});
		$("#video-controls").removeClass("fade");
	})


	$("#seekthumb").draggable({axis:"x",containment:"parent"})
	$("#seekthumb").mouseup(function(){
		var pos = $(this).position().left;
		var value = (pos/(($("#seeklength").width())-15)) * 100;
		$("#seek-bar").attr("value",value);
		var time = video.duration * (parseFloat($("#seek-bar").attr("value")) / 100);
		video.currentTime = time;
	})
	/*
	$("#volumethumb").draggable({axis:"x",containment:"parent"})
	$("#volumethumb").mouseup(function(){
		var pos = $(this).position().left;
		var value = Math.round((pos/(($("#volumelength").width())))*10)/10;
		$("#volume-bar").attr("value",value);
		video.volume = value;
	})
	$("#volumethumb").css({left:(($("#volumelength").width()))})

	$("video").bind("contextmenu",function(){
		return false;
	});*/

	$("#mute").click(function(){
		if(video.volume>0){
			$("#mute span").removeClass("glyphicon-volume-up");
			$("#mute span").addClass("glyphicon-volume-off");
			video.volume = 0;
		}else{
			$("#mute span").removeClass("glyphicon-volume-off");
			$("#mute span").addClass("glyphicon-volume-up");
			video.volume = 1;
		}
	})

	$("#full-screen").click(function(){
		if (!document.mozFullScreen && !document.webkitFullScreen) {
			if (video.requestFullscreen) {
				video.requestFullscreen();
			} else if (video.mozRequestFullScreen) {
				video.mozRequestFullScreen();
			} else if (video.webkitRequestFullscreen) {
				video.webkitRequestFullscreen(); 
			}
			document.mozFullScreen = true;
			document.webkitFullScreen = true;
		}else{
			if (document.mozCancelFullScreen) {
				document.mozCancelFullScreen();
			} else {
				document.webkitCancelFullScreen();
			}
			document.mozFullScreen = false;
			document.webkitFullScreen = false;
		}
	})

	

	$(document).on('webkitfullscreenchange mozfullscreenchange fullscreenchange', function(e){
		var state = document.fullScreen || document.mozFullScreen || document.webkitIsFullScreen;
		var event = state ? 'FullscreenOn' : 'FullscreenOff';
		if(event == "FullscreenOff"){
			$("#full-screen #up").show();
			$("#full-screen #down").hide();
		}else{
			$("#full-screen #down").show();
			$("#full-screen #up").hide();
		}
	});

	$("#seeklength").click(function(e){
		var mouseX = e.clientX;
		var pos = $("#seeklength").offset().left;
		var wid = mouseX - pos;
		var value = (wid/(($("#seeklength").width())-15)) * 100;
		$("#seek-bar").attr("value",value);
		var time = video.duration * (parseFloat($("#seek-bar").attr("value")) / 100);
		video.currentTime = time;
	})

},2000)

function timeFormat(time,duration){
	if(duration>=3600){
		var hours = parseInt( time / 3600 ) % 24;
		var minutes = parseInt( time / 60 ) % 60;
		var seconds = parseInt(time % 60);

		var result = (hours < 10 ? "0" + hours : hours) + ":" + (minutes < 10 ? "0" + minutes : minutes) + ":" + (seconds  < 10 ? "0" + seconds : seconds);
		return result;
	}else{
		var minutes = parseInt( time / 60 ) % 60;
		var seconds = parseInt(time % 60);

		var result = (minutes < 10 ? "0" + minutes : minutes) + ":" + (seconds  < 10 ? "0" + seconds : seconds);
		return result;
	}
}
