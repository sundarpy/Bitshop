/*Drop Down js start*/
	$('ul.nav li.dropdown').hover(function() {
	  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
	}, function() {
	  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
	});

/*drop down js end*/


/*slider add js start*/
$(document).ready( function() {
    $('#myCarousel').carousel({
		interval:   4000
	});
	
	var clickEvent = false;
	$('#myCarousel').on('click', '.nav a', function() {
			clickEvent = true;
			$('.nav li').removeClass('active');
			$(this).parent().addClass('active');		
	}).on('slid.bs.carousel', function(e) {
		if(!clickEvent) {
			var count = $('.nav').children().length -1;
			var current = $('.nav li.active');
			current.removeClass('active').next().addClass('active');
			var id = parseInt(current.data('slide-to'));
			if(count == id) {
				$('.nav li').first().addClass('active');	
			}
		}
		clickEvent = false;
	});
});
/*slider add js end*/

/*owl carousel script start*/
$(document).ready(function() {
 
  $("#owl-demo").owlCarousel({
 
      navigation : true, // Show next and prev buttons
      pagination:false,
      slideSpeed : 300,
      paginationSpeed : 400,
      navigationText:["<i class='fa fa-chevron-left' aria-hidden='true'></i>","<i class='fa fa-chevron-right' aria-hidden='true'></i>"],
      items : 5
 
  });
 
});
/*owl carousel script end*/

/*owl-demo-on carousel script start*/
$(document).ready(function() {
 
  $("#owl-demo-on").owlCarousel({
 
      navigation : true, // Show next and prev buttons
      pagination:false,
      slideSpeed : 300,
      paginationSpeed : 400,
	  navigationText:["<i class='fa fa-chevron-left' aria-hidden='true'></i>","<i class='fa fa-chevron-right' aria-hidden='true'></i>"],
      items : 6
 
  });
 
});
/*owl-demo-on  carousel script end*/
/*owl-demo-on carousel script start*/
$(document).ready(function() {
 
  $("#owl-demo-one").owlCarousel({
 
      navigation : true, // Show next and prev buttons
      pagination:false,
      slideSpeed : 300,
      paginationSpeed : 400,
	  navigationText:["<i class='fa fa-chevron-left' aria-hidden='true'></i>","<i class='fa fa-chevron-right' aria-hidden='true'></i>"],
      items : 6
 
  });
 
});
/*owl-demo-on  carousel script end*/
/*owl-demo-on carousel script start*/
$(document).ready(function() {
 
  $("#owl-demo-two").owlCarousel({
 
      navigation : true, // Show next and prev buttons
      pagination:false,
      slideSpeed : 300,
      paginationSpeed : 400,
	  navigationText:["<i class='fa fa-chevron-left' aria-hidden='true'></i>","<i class='fa fa-chevron-right' aria-hidden='true'></i>"],
      items : 6
 
  });
 
});
/*owl-demo-on  carousel script end*/
/*owl-demo-on carousel script start*/
$(document).ready(function() {
 
  $("#owl-demo-three").owlCarousel({
 
      navigation : true, // Show next and prev buttons
      pagination:false,
      slideSpeed : 300,
      paginationSpeed : 400,
	  navigationText:["<i class='fa fa-chevron-left' aria-hidden='true'></i>","<i class='fa fa-chevron-right' aria-hidden='true'></i>"],
      items : 6
 
  });
 
});
/*owl-demo-on  carousel script end*/
/*owl-demo-on carousel script start*/
$(document).ready(function() {
 
  $("#owl-demo-four").owlCarousel({
 
      navigation : true, // Show next and prev buttons
      pagination:false,
      slideSpeed : 300,
      paginationSpeed : 400,
	  navigationText:["<i class='fa fa-chevron-left' aria-hidden='true'></i>","<i class='fa fa-chevron-right' aria-hidden='true'></i>"],
      items : 6
 
  });
 
});

$(document).ready(function() {
 
  $("#owl-demo-five").owlCarousel({
 
      navigation : true, // Show next and prev buttons
      pagination:false,
      slideSpeed : 300,
      paginationSpeed : 400,
    navigationText:["<i class='fa fa-chevron-left' aria-hidden='true'></i>","<i class='fa fa-chevron-right' aria-hidden='true'></i>"],
      items : 6
 
  });
 
});
/*owl-demo-on  carousel script end*/
/*owl-demo-on carousel script start*/
$(document).ready(function() {
 
  $("#owl-demo-items").owlCarousel({
 
      navigation : true, // Show next and prev buttons
      pagination:false,
      slideSpeed : 300,
      paginationSpeed : 400,
    navigationText:["<i class='fa fa-chevron-left' aria-hidden='true'></i>","<i class='fa fa-chevron-right' aria-hidden='true'></i>"],
      items : 2
 
  });
 
});
/*owl-demo-on  carousel script end*/

/*more content js start*/
$(document).ready(function() {
    // Configure/customize these variables.
    var showChar = 100;  // How many characters are shown by default
    var ellipsestext = "...";
    var moretext = "Show more >";
    var lesstext = "Show less";
    

    $('.more').each(function() {
        var content = $(this).html();
 
        if(content.length > showChar) {
 
            var c = content.substr(0, showChar);
            var h = content.substr(showChar, content.length - showChar);
 
            var html = c + '<span class="moreellipses">' + ellipsestext+ '&nbsp;</span><span class="morecontent"><span>' + h + '</span>&nbsp;&nbsp;<a href="" class="morelink">' + moretext + '</a></span>';
 
            $(this).html(html);
        }
 
    });
 
    $(".morelink").click(function(){
        if($(this).hasClass("less")) {
            $(this).removeClass("less");
            $(this).html(moretext);
        } else {
            $(this).addClass("less");
            $(this).html(lesstext);
        }
        $(this).parent().prev().toggle();
        $(this).prev().toggle();
        return false;
    });
});
/*more content js end*/
