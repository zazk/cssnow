// JavaScript Document
$(function(){
  var j = 0;
  var i = 0;
  setInterval(function(){$('body').css('background-position', i++ )},50)
  setInterval(function(){$('#wrap').css('background-position', j-- )},50)
});