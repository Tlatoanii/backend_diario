import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import random
from art import text2art

class Logger():
    sub_lista = ["3-d","d_diagonal","4x4_offr","acrobatic","alligator","alligator2","alligator3","alpha","amcneko","amcrazor","amcun1","arrows","atc_gran","avatar","banner3-d",
                "bear","big","bigchief","block","braced","broadway","bulbhead","calgphy2","caligraphy","cards","catwalk","chiseled","chunky","cola","colossal","computer","contrast",
                "crawford","cricket","cybermedium","dancingfont","defleppard","digital","doh","doom","dotmatrix","double","eftirobot","epic","fantasy1","fire_font-s","flipped",
                "fraktur","funface","future_1","fuzzy","georgi16","georgia11","ghost","ghoulish","goofy","gothic","graceful","gradient","graffiti","henry3d","hollywood","horizontalleft",
                "horizontalright","impossible","invita","isometric1","isometric2","isometric3","isometric4","jacky","jazmine","keyboard","larry3d","lean","lildevil","lineblocks",
                "marquee","merlin1","merlin2","modular","nancyj","nancyj-fancy","nancyj-underlined","nscript","nvscript","o8","ogre","pawp","peaks","poison","puffy","puzzle","rammstein",
                "rectangles","red_phoenix","roman","rounded","rowancap","sblood","serifcap","slant","small","smallcaps","smisome1","smkeyboard","smpoison","soft","speed","stacey","standard",
                "starwars","stop","sub-zero","swampland","sweet","tarty1","tarty8","tarty9","ticksslant","twisted","varsity","wetletter","whimsy"]
    
    def __init__(self, log_path):
        # Verificar si la carpeta logs existe, si no, crearla
        self.file_path = Path(log_path).resolve()
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.logger = logging.getLogger(self.file_path.name)
        self.logger.setLevel(logging.INFO)
        
        if not self.logger.hasHandlers():
            handler = RotatingFileHandler(
                self.file_path, 
                maxBytes=5*1024*1024, 
                backupCount=3,
                encoding='utf-8'
            )
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def logTitle(self, message):
        message = f"\n {message} "
        font = random.choice(self.sub_lista)
        self.logger.info(text2art(message, font= font ))
    
    def logInfo(self, message):
        self.logger.info(message)
        
    def logError(self, message):
        self.logger.error(message)
        
    def logWarning(self, message):
        self.logger.warning(message)
        
    def logDebug(self, message):
        self.logger.debug(message) 
    
    def close(self):
        self.logger.info('Closing sample program')