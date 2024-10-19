from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import cv2
from pyzbar import pyzbar

class QRReaderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Esperando código QR...")
        self.layout.add_widget(self.label)

        # Usar el método update en intervalos regulares
        Clock.schedule_interval(self.update, 1.0 / 30.0)
        return self.layout

    def update(self, dt):
        # Abrir la cámara y leer un frame
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        if ret:
            # Detectar códigos QR
            qr_codes = pyzbar.decode(frame)

            if qr_codes:
                for qr_code in qr_codes:
                    qr_data = qr_code.data.decode('utf-8')
                    self.label.text = f"QR Data: {qr_data}"

            # Cerrar la cámara
            cap.release()

if __name__ == '__main__':
    QRReaderApp().run()
