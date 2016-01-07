$(document).ready(function(){

    Navbar();
    DeployArticle();
    $(window).load(function(){
        adapt_form_width();
        toggle_navbar_form();
        if(window.location.pathname == '/'){
            AbonnementBtn(true);
        }else{  
            AbonnementBtn(false);
        }
    });
    $('.caption-screen').first().addClass('first');
});

$(window).resize(function(){
    Navbar();
    adapt_form_width();
    toggle_navbar_form();
    if($(window).width()<970){
        $('#banner_layer').height(($('#contentNav').outerWidth()/970)*150+'px');
    }else{
        $('#banner_layer').height(150);
    }
    AbonnementBtn(false);
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

function AbonnementBtn(animation){
    referent = $('#abonnement');
    aboReferent = $('.navbar-header');
    aboHeight = $('#contentNav').outerHeight()-2;
    aboWidth = $('.navbar-brand img').width();
    aboPositionReferent = aboReferent.offset();
    aboX = aboPositionReferent.left +2;
    aboY = aboPositionReferent.top;
    if(animation==true){
        referent.width(aboWidth).css({left: aboX}).css({top: aboY+aboHeight-40});
        setTimeout(function(){
            referent.css({top: aboY+aboHeight})
        },1500);
    }else{
        referent.width(aboWidth).css({left: aboX}).css({top: aboY+aboHeight});
    }
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


// new navbar form
function adapt_form_width(){
    target = $('.navbar-form');
    referent = $('#contentNav .container');
    subTarget = $('.navbar-form .form-group .form-control');
    if($(window).width() > 768){
        target.height(referent.height());
        subTarget.width($('.navbar-nav:first').outerWidth()).height(referent.outerHeight()).css('margin-left',$('.navbar-header').width()-15);
    }else{
        target.width(referent.outerWidth()).height();
        // subTarget.width(referent.width() - $('#search-btn').outerWidth() +2).height(50);
    }
}

function toggle_navbar_form(){
    $('#search-btn, #close-btn-2').click(function(){
        if($('#search_form').hasClass('hide')){
            $('#search_form').removeClass('hide');
            $('#search_form input').focus();
            $('#search-btn a i').removeClass('fa-search').addClass('fa-close');
        }else{
            $('#search_form').addClass('hide');
            $('#search-btn a i').removeClass('fa-close').addClass('fa-search');
        }
    });
}
// ./new navbar form




