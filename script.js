const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

const WIDTH = canvas.width;
const HEIGHT = canvas.height;
const BAR_WIDTH = 5;
const ARRAY_SIZE = Math.floor(WIDTH / BAR_WIDTH);
const array = Array.from({ length: ARRAY_SIZE }, (_, i) => Math.random() * HEIGHT);

function drawArray(array) {
    ctx.clearRect(0, 0, WIDTH, HEIGHT);
    array.forEach((value, index) => {
        ctx.fillStyle = '#3498db';
        ctx.fillRect(index * BAR_WIDTH, HEIGHT - value, BAR_WIDTH, value);
    });
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function bubbleSort() {
    let arr = [...array];
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = 0; j < arr.length - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                drawArray(arr);
                await sleep(50);
            }
        }
    }
}

function randomizeArray() {
    for (let i = 0; i < ARRAY_SIZE; i++) {
        array[i] = Math.random() * HEIGHT;
    }
    drawArray(array);
}

function startBubbleSort() {
    randomizeArray();
    bubbleSort();
}

// Initial draw
drawArray(array);
