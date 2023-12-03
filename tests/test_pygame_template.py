import pygame
import pytest
from unittest.mock import patch, MagicMock
from GameEngine.loop import Game


def test_start_game():
    with patch('pygame.init') as mock_init, \
            patch('pygame.display.set_mode') as mock_set_mode, \
            patch('pygame.event.get') as mock_event_get, \
            patch('pygame.draw.circle') as mock_draw_circle, \
            patch('pygame.display.flip') as mock_display_flip, \
            patch('pygame.quit') as mock_quit:
        # Mocking Pygame functions
        mock_event = MagicMock()
        mock_event.type = pygame.QUIT
        mock_event_get.return_value = [mock_event]
        mock_set_mode.return_value = MagicMock()

        # Running the game loop
        Game.start_game()

        # Assertions
        mock_init.assert_called_once()
        mock_set_mode.assert_called_once_with([500, 500])
        mock_event_get.assert_called_once()
        mock_draw_circle.assert_called_once()
        mock_display_flip.assert_called_once()
        mock_quit.assert_called_once()
