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

Dropzone.options.myGreatDropzone = { 
    url: "upload/",
    maxFiles: 100,
    acceptedFiles: 'image/png, .jpg, .jpeg, .docx',
    parallelUploads:100,
    uploadMultiple:true,
    timeout:180000,
    init: function () {
        this.on("complete", function (file) {
          if (this.getUploadingFiles().length === 0 && this.getQueuedFiles().length === 0) {
            // window.location = "/mygallery"
            return 1
          }
        });
      }
  };


if (readyZip) {
    console.log("true")
} else {
    console.log("false")   
}