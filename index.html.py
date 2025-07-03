from pynput import keyboard

buffer = ""

def on_press(key):
    global buffer
    try:
        buffer += key.char  # Добавляем вводимый символ
    except AttributeError:
        if key == keyboard.Key.enter:
            if buffer:
                print(f"📦 Считан штрихкод: {buffer}")
                buffer = ""

print("🟢 Ожидание ввода с HID-сканера... (нажми Ctrl+C для выхода)")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
