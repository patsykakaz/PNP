$(document).ready(function(){


    //
    // parent = $('.navbar-collapse .container');
    // parentW = parent.width();
    // catDrop = $('.dropdown-category');
    // highlightsDrop = $('.dropdown-highlights');
    // logoDrop = $('.dropdown-logo');

    // catDrop.width($('.navbar-brand').outerWidth());
    // if($(window).width() > 768){
    //     logoDrop.width(parentW*0.3);
    // }else{
    //     logoDrop.css('display','none');
    // }
    // highlightsDrop.width(parentW*0.7-(logoDrop.outerWidth()+5));
    // highlightsDrop.css('margin-left','-5px');
    Navbar();
    $(window).load(function(){
        // MainArticles();
    });
    DeployArticle();
    $('.caption-screen').first().addClass('first');
    $('.bloc_article').mouseover(function(){
        target = $(this).children('.label');
        setInterval(function(){
            target.addClass('hoverClass');
                setTimeout(function(){
                    target.removeClass('hoverClass');
                },500);
        },1000);
    });
});

$(window).resize(function(){
    Navbar();
        if($(window).width()<970){
            $('#banner_layer').height(($('#contentNav').outerWidth()/970)*150+'px');
        }else{
	    $('#banner_layer').height(150);
        }
});

function Navbar(){
    if($(window).width() < 992){
        $('.highlight-box:eq(2)').addClass('hide');
    }else{
        $('.highlight-box:eq(2)').removeClass('hide');
    }

    $("*").each(function(){
        if($(this).outerWidth()>$(window).width()){
            // alert($(this).attr('class'));
        }
    });
}

function MainArticles(){
    currentLeft = 0;
    $('.container-mainArticle').each(function(){
        $(this).css('left',currentLeft+'%');
	if($(this).hasClass('deploy')){
	    currentLeft += 50;
	}else{
            currentLeft += 50;
	}
        console.log($(this).outerWidth());
    });
}
function DeployArticle(){
    $('.container-mainArticle').mouseover(function(){
        if(!$(this).hasClass('deploy')){
            $('.container-mainArticle').not($(this)).removeClass('deploy');
            $(this).addClass('deploy');
            $('#mainArticles').toggleClass('left');
        }
    });
}






