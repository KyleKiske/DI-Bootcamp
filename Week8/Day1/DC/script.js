class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }

  watch(){
    console.log(`${this.uploader} watched all ${this.time} of ${this.title}!`);
  }
}

const potion = new Video("Potion Seller", "Justin Kuritzkes", 187);
potion.watch();

const drive = new Video("Drive", "Gosling", 6800);
drive.watch();

let videoList = [
  {title : "Bahrain", uploader : "Max", time: 5400},
  {title : "Monza", uploader : "Lewis", time: 5000},
  {title : "Spa", uploader : "Michael", time: 9600},
  {title : "Monaco", uploader : "Chuck", time: 7260},
  {title : "Interlagos", uploader : "Seb", time: 5300}
];

let videos = videoList.map((info) => new Video(info.title, info.uploader, info.time));

for (const video of videos) {
    video.watch();
}