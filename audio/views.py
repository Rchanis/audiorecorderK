from azure.storage.blob import BlobServiceClient
from django.shortcuts import render
import os


def home(request):
    return render(request, "index.html")


def song(request):
    connection_string = os.environ.get("AZURE_STORAGEBLOB_CONNECTIONSTRING")
    container_name = "audios"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    audio_files = []

    for blob in container_client.list_blobs():
        audio_files.append(container_client.get_blob_client(blob.name).url)

    return render(request, "canciones.html", {"audio_files": audio_files})


def record(request):
    return render(request, "grabar.html")
