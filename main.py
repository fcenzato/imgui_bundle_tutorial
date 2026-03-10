from imgui_bundle import imgui, imgui_ctx, immapp

value = 0.5
checked = False
text = "Hello"


def gui():
    global value, checked, text

    imgui.text("Hello, world!")

    if imgui.button("Click me"):
        print("Button clicked!")

    changed, value = imgui.slider_float("Value", value, 0.0, 1.0)
    changed, checked = imgui.checkbox("Enable", checked)
    changed, text = imgui.input_text("Name", text)

    # The button returns True when clicked
    if imgui.button("Save"):
        print("Saving a file")

    # Sliders return (changed, new_value)
    changed, value = imgui.slider_float("Speed", value, 0.0, 100.0)
    if changed:
        print("Speed updated to", value)

    imgui.button("OK")
    imgui.button("OK##dialog2")

    for i in range(3):
        imgui.push_id(i)
        imgui.button("Button")  # IDs are "0/Button", "1/Button", "2/Button"
        imgui.pop_id()

    with imgui_ctx.begin("My Window") as window_opened:
        if window_opened:
            imgui.text("Content here")


immapp.run(gui, window_title="ImGui Demo")
