import os
from PIL import Image


def convert_to_png(input_path):
  """
  Converts a single image file to PNG format and saves it in the same folder.

  Args:
      input_path: Path to the image file to be converted.

  Returns:
      True if conversion is successful, False otherwise.

  Raises:
      OSError: If an error occurs while processing the image.
  """

  # Extract filepath and extension
  base, ext = os.path.splitext(input_path)
  # Check if the file is an image using its extension (common image formats)
  if ext.lower() not in (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"):
    # print(f"Skipping non-image file: {filename}")
    return False

  # Create output filename with PNG extension (same folder as input)
  output_path = f"{base}.png"  # Replace original extension with PNG

  try:
    # Open the image using Pillow
    img = Image.open(input_path)

    # Convert to RGB mode (if necessary) for PNG compatibility
    if img.mode != "RGB":
      img = img.convert("RGB")

    # Save the image as PNG with optimal quality (same folder)
    img.save(output_path, "PNG", quality=100)  # Adjust quality as needed
    # print(f"Converted: {input_path} -> {output_path}")

    return output_path  # Indicate success

  except (IOError, OSError) as e:
    # print(f"Error converting {filename}: {e}")
    return False  # Indicate error
