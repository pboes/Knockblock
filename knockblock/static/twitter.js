   jQuery(document).ready(addClickHandlers());


   var output = "";

   function addClickHandlers() {

     jQuery('#twitter').on("submit", function(event) {
       event.preventDefault();
       var input = $("#twitter").serializeArray(); //+ "=" + $(this).val();
       jQuery.ajax({
         url: "twitter_start",
         type: "POST",
         data: {
           "input": input[1].value
         },
       }).done(function(task) {
         console.log(task);
         output = JSON.parse(task);
         //console.log(output);
         return twitter_task(output.job);
       })

     });



     jQuery('#revoke').on("click", function(event) {
       event.preventDefault();
       // $( window ).unload(function() {
       // return "Bye now!";
       console.log(output.job)
       jQuery.ajax({
         url: "twitter_stop",
         type: "POST",
         data: {
           "id": output.job
         }
         //"task_id":task_id,
       }).done(function(task) {
         window.location.href = "";
       })
     });
   }

   // jQuery('#twitter').on("submit", function(event){
   //     event.preventDefault();
   // // onload=function() {


   function twitter_task(task_id) {
     var SearchState = function() {
       jQuery.ajax({
         url: "twitter_update",
         type: "GET",
         data: {}
         //"task_id":task_id,
       }).done(function(task) {

         //console.log(task);
         jQuery('.display').html(task); //.substr(0,task.length)
         // console.log(task.substr(2,L));

         var timer = setTimeout(SearchState, 100);
       });
     };

     SearchState();
   }

   // }

   // This code is a snippet that makes sure the csrf token is somehow passed from the initial view to the ajaxview, since these cannot be passed on by the jquery...
   $(function() {


     // This function gets cookie with a given name
     function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
           var cookie = jQuery.trim(cookies[i]);
           // Does this cookie string begin with the name we want?
           if (cookie.substring(0, name.length + 1) == (name + '=')) {
             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
             break;
           }
         }
       }
       return cookieValue;
     }
     var csrftoken = getCookie('csrftoken');

     /*
     The functions below will create a header with csrftoken
     */

     function csrfSafeMethod(method) {
       // these HTTP methods do not require CSRF protection
       return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
     }

     function sameOrigin(url) {
       // test that a given url is a same-origin URL
       // url could be relative or scheme relative or absolute
       var host = document.location.host; // host + port
       var protocol = document.location.protocol;
       var sr_origin = '//' + host;
       var origin = protocol + sr_origin;
       // Allow absolute or scheme relative URLs to same origin
       return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
         (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
         // or any other URL that isn't scheme relative or absolute i.e relative.
         !(/^(\/\/|http:|https:).*/.test(url));
     }

     $.ajaxSetup({
       beforeSend: function(xhr, settings) {
         if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
           // Send the token to same-origin, relative URLs only.
           // Send the token only if the method warrants CSRF protection
           // Using the CSRFToken value acquired earlier
           xhr.setRequestHeader("X-CSRFToken", csrftoken);
         }
       }
     });


   });
