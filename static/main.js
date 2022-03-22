var readyZip = false



function myGreeting() {
  
  swal({
      title: "Successful organization",
      text: "Your images is now organized by similarity. Check it out in your collection tab!",
      icon: "success",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete) => {
      if (willDelete) {
        window.location.href = "/collection";
      } else {
        // swal("Your imaginary file is safe!");
        return 0
      }
    });


}


function myGreetingGuest() {
  
    window.location.href = "/guestalbum";

}



function badFile() {
  swal("Oops...", "This file is not valid, only image", "error");
}



Dropzone.options.myGreatDropzone = { 
    url: "upload/",
    maxFiles: 100,
    acceptedFiles: 'image/png, .jpg, .jpeg',
    maxFilesize: 5,
    parallelUploads:100,
    uploadMultiple:true,
    timeout:180000,
    init: function () {
        this.on("success", function (file) {
          if (this.getUploadingFiles().length === 0 && this.getQueuedFiles().length === 0) {
            setTimeout(myGreeting, 1000);
          }
        });
        this.on("error", function (file) {
          if (this.getUploadingFiles().length === 0 && this.getQueuedFiles().length === 0) {
            setTimeout(badFile, 1000);
            
          }
        });
      }
  };



  Dropzone.options.myGreatDropzone = { 
    url: "guestupload/",
    maxFiles: 100,
    acceptedFiles: 'image/png, .jpg, .jpeg',
    maxFilesize: 5,
    parallelUploads:100,
    uploadMultiple:true,
    timeout:180000,
    init: function () {
        this.on("success", function (file) {
          if (this.getUploadingFiles().length === 0 && this.getQueuedFiles().length === 0) {
            setTimeout(myGreetingGuest, 1000);
          }
        });
        this.on("error", function (file) {
          if (this.getUploadingFiles().length === 0 && this.getQueuedFiles().length === 0) {
            setTimeout(badFile, 1000);
            
          }
        });
      }
  };




