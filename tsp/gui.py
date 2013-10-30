import pygame

class GUI(object):
  @classmethod
  def setup_screen(cls):
    info = pygame.display.Info()
    size = min(info.current_w, info.current_h) - 100
    screen = pygame.display.set_mode((size, size))
    return screen
 
  def __init__(self, graph):
    self.graph = graph
    pygame.init()
    self.screen = GUI.setup_screen()
    self.max_node = (max(graph.nodes.itervalues(), key=lambda n: n[0])[0],
                     max(graph.nodes.itervalues(), key=lambda n: n[1])[1])
    self.min_node = (min(graph.nodes.itervalues(), key=lambda n: n[0])[0],
                     min(graph.nodes.itervalues(), key=lambda n: n[1])[1])
    self.diff_node = (self.max_node[0] - self.min_node[0], 
                      self.max_node[1] - self.min_node[1])

    self.draw_map(True)

  def draw_map(self, blit):
    self.screen.fill((255,255,255))
    map(self.draw_node, self.graph.nodes.iteritems())
    if blit:
      pygame.display.flip()

  def draw_node(self, (id,node)):
    pygame.draw.circle(self.screen, (255, 0, 0), self.get_coords(node), 3)

  def get_coords(self, (x,y)):
    (x, y) = self.scale((x,y), self.min_node, self.diff_node)
    return (int(x * self.screen.get_height() - 10) + 5,
            int(y * self.screen.get_width()  - 10) + 5)

  def scale(self, (x, y), (min_x, min_y), (diff_x, diff_y)):
    return ((x - min_x) / diff_x, (y - min_y) / diff_y)

  def draw_path(self, path, colour):
    path_forward = path[1:] + path[:1]
    for (i,j) in zip(path, path_forward):
      pygame.draw.aaline(self.screen, colour, 
                         self.get_coords(self.graph.nodes[i]),
                         self.get_coords(self.graph.nodes[j]))

  def update_map(self, best):
    self.draw_map(False)
    self.draw_path(best[0].genes, (0, 0, 0))
    text = pygame.font.Font(pygame.font.get_default_font(), 12)
    t = text.render("Best distance: {}".format(best[0].score), True, (0,0,0))
    self.screen.blit(t, (0,0))
    pygame.display.flip()
  
