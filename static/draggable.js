// Function to set the current year
function setCurrentYear() {
    const currentYear = new Date().getFullYear();
    document.querySelectorAll('#current-year').forEach(element => {
        element.textContent = currentYear;
    });
}


//mood
document.getElementById('submitButton').addEventListener('click', function() {
    var radioButtons = document.querySelectorAll('input[name="fieldset-example2"]');
    for (var i = 0; i < radioButtons.length; i++) {
      if (radioButtons[i].checked) {
        alert('You are feeling ' + radioButtons[i].value + ' today.');
        break;
      }
    }
  });

document.querySelectorAll('.draggable').forEach(draggable => {
    const titleBar = draggable.querySelector('.title-bar');

    // Add drag functionality to the title bar
    function onDragStart(event) {
        event.preventDefault();

        let shiftX, shiftY;

        if (event.type === 'mousedown') {
            shiftX = event.clientX - draggable.getBoundingClientRect().left;
            shiftY = event.clientY - draggable.getBoundingClientRect().top;
        } else if (event.type === 'touchstart') {
            const touch = event.touches[0];
            shiftX = touch.clientX - draggable.getBoundingClientRect().left;
            shiftY = touch.clientY - draggable.getBoundingClientRect().top;
        }

        function moveAt(pageX, pageY) {
            draggable.style.left = pageX - shiftX + 'px';
            draggable.style.top = pageY - shiftY + 'px';
        }

        function onMouseMove(event) {
            moveAt(event.pageX, event.pageY);
        }

        function onTouchMove(event) {
            const touch = event.touches[0];
            moveAt(touch.pageX, touch.pageY);
        }

        function onStop() {
            document.removeEventListener('mousemove', onMouseMove);
            document.removeEventListener('touchmove', onTouchMove);
            document.removeEventListener('mouseup', onStop);
            document.removeEventListener('touchend', onStop);
        }

        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('touchmove', onTouchMove);
        document.addEventListener('mouseup', onStop);
        document.addEventListener('touchend', onStop);
    }

    titleBar.addEventListener('mousedown', onDragStart);
    titleBar.addEventListener('touchstart', onDragStart);

    draggable.ondragstart = function() {
        return false;
    };

    // Add close button functionality
    const closeButton = draggable.querySelector('button[aria-label="Close"]');
    closeButton.addEventListener('click', () => {
        draggable.style.display = 'none';
        setTimeout(() => {
            draggable.style.display = 'block';
        }, 1000); // 1 second
    });
});


function displayDivsInOrder() {
    const mainSection = document.getElementById('main');
    const mainRect = mainSection.getBoundingClientRect();

    const draggables = Array.from(document.querySelectorAll('.draggable'))
        .sort((a, b) => a.dataset.id - b.dataset.id); // Sort by data-id

    draggables.forEach((draggable, index) => {
        setTimeout(() => {
            const maxWidth = (window.innerWidth * 2 / 3) - draggable.clientWidth;
            const maxHeight = (window.innerHeight * 2 / 3) - draggable.clientHeight;
            const randomX = Math.floor(Math.random() * maxWidth);
            const randomY = Math.floor(Math.random() * maxHeight);

            draggable.style.left = randomX + 'px';
            draggable.style.top = randomY + 'px';
            draggable.style.zIndex = index + 1; // Increase z-index
            draggable.style.display = 'block'; // Make visible
        }, index * 100); // 0.2 seconds interval
    });
}

window.onload = () => {
    setCurrentYear();
    displayDivsInOrder();
};

window.onresize = displayDivsInOrder; // Recalculate positions on window resize
