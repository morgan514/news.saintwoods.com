document.addEventListener('DOMContentLoaded', function() {
    const popoutDivLeft = document.getElementById('popout-div-left');
    const popoutDivRight = document.getElementById('popout-div-right');


    setTimeout(function() {
        popoutDivLeft.classList.remove('hidden');
        popoutDivLeft.classList.add('visible');
    }, 1000);


    popoutDivLeft.addEventListener('click', function() {
        popoutDivLeft.classList.remove('visible');
        popoutDivLeft.classList.add('hidden');

        setTimeout(function() {
            popoutDivLeft.classList.remove('hidden');
            popoutDivLeft.classList.add('visible');
        }, 5000);
    });

    setTimeout(function() {
        popoutDivRight.classList.remove('hidden');
        popoutDivRight.classList.add('visible');
    }, 3000);


    popoutDivRight.addEventListener('click', function() {
        popoutDivRight.classList.remove('visible');
        popoutDivRight.classList.add('hidden');
        
      
        setTimeout(function() {
            popoutDivRight.classList.remove('hidden');
            popoutDivRight.classList.add('visible');
        }, 5000);
    });
});
