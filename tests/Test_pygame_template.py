import sys
import pygame
from io import StringIO # Replace with the actual name of your script's main function

def test_main_function(capsys):
    pygame.init()

    # Redirect stdout to capture print statements
    sys.stdout = StringIO()

    # Get the output from print statements
    captured = capsys.readouterr()

    # Reset sys.stdout
    sys.stdout = sys.__stdout__

    # Assert that the output or behavior matches your expectations
    assert captured.out.strip() == "Expected output or behavior"


def test_draw_circle():
    pygame.init()

    # Create a surface to draw on
    test_surface = pygame.Surface((500, 500))

    # Draw a circle on the surface
    pygame.draw.circle(test_surface, (0, 0, 255), (250, 250), 75)

    # Get the color of a pixel at the center of the circle
    pixel_color = test_surface.get_at((250, 250))

    # Assert that the pixel color matches your expectations
    assert pixel_color == (0, 0, 255, 255)
