# Day 07 - Processing

## Intro to graphical thinking

1. The canvas is a grid of pixels `width` wide and `height` tall.
  - Coordinate 0,0 is at the top left of the screen.
  - Coordinate *width*,*height* is at the bottom right of the screen
2. Colours
  - R, G, B `(255,146,37)` or greyscale `(255)`.
  - Range from 0 to 255. 
  - `fill()` colours in shapes and `stroke()` outlines them.
3. Order of operations matters; the last thing drawn will be "on top"
4. Shapes
  - `line()` takes 4 arguments: xpos1, ypos1, xpos2, ypos2
  - `ellipse()` takes 4 arguments: xpos (*center*), ypos (*center*), width, height
  - `rect()` takes 4 arguments: xpos (*top left corner*), ypos (*top left corner*)

## Intro to animation


## Intro to Game Making

1. Scope. Keep it simple at first.
2. Single purpose functions

## Making a game

1. Start with the player movement. Is that mechanic enjoyable?
  - Use `keyPressed` to determine if key has been pressed.
  - Add acceleration and velocity to the movement.
2. Create some asteroids
  - Asteroid coordinates in a list
  - Move asteroids
  - Draw asteroids
  - Add details like speed, size, via asteroids list
3. Collision Detection
  - Bouning box/bounding circle.
  - `dist` between two center points. If less than the 2 radiuses added together, collision.