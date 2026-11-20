import pygame
from shot import Shot
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS

class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: "screen") -> None:
        pygame.draw.polygon(screen, "cyan", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> float:
        self.rotation += (PLAYER_TURN_SPEED * dt)

        return self.rotation

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            # left
            self.rotate(-dt)

        if keys[pygame.K_RIGHT]:
            # right
            self.rotate(dt)

        if keys[pygame.K_UP]:
            # forward
            self.move(dt)

        if keys[pygame.K_DOWN]:
            # backward
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            # shoot
            self.shoot_timer -= dt
            self.shoot()
        

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        if self.shoot_timer > 0:
            return

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
