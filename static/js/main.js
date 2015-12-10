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
        MainArticles();
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
    deployElementIndex = 
    $('.mainArticle').each(function(){
        $(this).css('left',currentLeft+'%');
	if($(this).hasClass('deploy')){
	    currentLeft += 70;
	}else{
            currentLeft += 30;
	}
        console.log($(this).outerWidth());
    });
}
function DeployArticle(targetID){
    target = $('.mainArticle:eq('+targetID+')');
    $('.mainArticle').removeClass('deploy');
    target.addClass('deploy');
    setTimeout(function(){
        MainArticles();
    },200);
}






