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
    // mainArticles();
});

$(window).resize(function(){
    Navbar();
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

// function mainArticles(){
//     $('.mainArticle img').each(function(){
//         parent = $(this).parent('.mainArticle');
//         $(this).offset({ top: (parent.height()-$(this).height())/2, left: (parent.width()-$(this).width())/2 });
//     });
// }