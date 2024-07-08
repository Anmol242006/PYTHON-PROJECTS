{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3ade7c3-2657-41b1-a33e-47e20b792e70",
   "metadata": {},
   "outputs": [],
   "source": [
    "import qrcode\n",
    "from PIL import Image\n",
    "\n",
    "qr=qrcode.QRCode(version=1,\n",
    "                 error_correction=qrcode.constants.ERROR_CORRECT_H,\n",
    "                 box_size=10,border=4,)\n",
    "qr.add_data(\"https://web.whatsapp.com\")\n",
    "qr.make(fit=True)\n",
    "img=qr.make_image(fill_color=\"red\",back_color=\"white\")\n",
    "img.save(\"youtube\")\n",
    "img.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
