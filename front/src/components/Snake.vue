<template>
    <canvas ref="canvas" width="400" height="400"></canvas>
</template>

<script>
    export default {
        name: "Snake",
        data: function () {
            return {
                playerX: 10,
                playerY: 10,
                velocityX: 0,
                velocityY: 0,
                appleX: 15,
                appleY: 15,
                trail: [],
                tail: 5,
                context: null,
                canvas: null,
                gridSize: 20,
                tileCount: 20
            }
        },
        methods: {
            drawBackground() {
                this.context.fillStyle = 'black';
                this.context.fillRect(0, 0, this.canvas.width, this.canvas.height);
            },
            drawSnake() {
                this.context.fillStyle = 'lime';
                for (let i = 0; i<this.trail.length; i++) {
                    this.context.fillRect(
                        this.trail[i].x * this.gridSize,
                        this.trail[i].y * this.gridSize,
                        this.gridSize - 2,
                        this.gridSize - 2
                    );
                }
                this.trail.push({x: this.playerX, y: this.playerY});
                while (this.trail.length > this.tail) {
                    this.trail.shift();
                }
            },
            drawApple() {
                this.context.fillStyle = 'red';
                this.context.fillRect(
                    this.appleX * this.gridSize,
                    this.appleY * this.gridSize,
                    this.gridSize - 2,
                    this.gridSize - 2
                );
            },
            onEatApple() {
                if (this.appleX === this.playerX && this.appleY === this.appleY) {
                    this.appleX = Math.floor(Math.random() * this.tileCount);
                    this.appleY = Math.floor(Math.random() * this.tileCount);
                }
            },
            drawGame(){
                this.drawBackground();
                this.drawSnake();
                this.drawApple();
                this.onEatApple();
                requestAnimationFrame(this.drawGame);
            },
            initElements() {
                this.canvas = this.$refs.canvas;
                this.context = this.canvas.getContext('2d');
            }
        },
        mounted() {
            this.initElements();
            requestAnimationFrame(this.drawGame);
        }
    }
</script>

<style scoped>
    canvas {
        border: 1px solid black;
    }
</style>