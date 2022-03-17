var app = new Vue({
	el: '#app',
	data: {
		task: 'Un task',
        mot: 'un mot',
	},

    methods:{

        popThis(){
            console.log("test")
            alert("test2")
        },

        unclick(){
            alert("test222")
        },

    }

})


var readyZip = false

function myGreeting() {
  swal("It's ready!", "Your images is now organized by similarity. Check it out in your collection tab!", "success");
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
            setTimeout(myGreeting, 2000);
            
          }
        });
        this.on("error", function (file) {
          if (this.getUploadingFiles().length === 0 && this.getQueuedFiles().length === 0) {
            setTimeout(badFile, 2000);
            
          }
        });
      }
  };



