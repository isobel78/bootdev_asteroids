import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(
        self,
        x: float,
        y: float,
        radius: float,
        color: str | tuple[int, int, int] = "hotpink"
        ) -> None:
        super().__init__(x, y, radius)
        self.color = color

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)
        

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        new_move_1 = self.velocity.rotate(angle)
        new_move_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        colors = ["orange", "skyblue", "lime", "purple"]
        new_asteroid_1 = Asteroid(
            self.position.x, self.position.y, new_radius, color=random.choice(colors)
        )
        new_asteroid_2 = Asteroid(
            self.position.x, self.position.y, new_radius, color=random.choice(colors)
        )

        new_asteroid_1.velocity = new_move_1 * 1.2
        new_asteroid_2.velocity = new_move_2 * 1.2
