import { assets } from "@/assets/img";
import { listReducer } from "./filter";

const reqImages = assets.devBenefits,
  joinCards = [
    {
      title: "hassle-free payments",
      desc:
        "The quick brown fox jumps over a lazy dog. \
     DJs flock by when MTV axquiz prog.",
      thumb: reqImages.pay,
    },
    {
      title: "iso-certified trainers",
      desc:
        "The quick brown fox jumps over a lazy dog. \
     DJs flock by when MTV axquiz prog.",
      thumb: reqImages.verified,
    },
    {
      title: "trial classes available",
      desc:
        "The quick brown fox jumps over a lazy dog. \
     DJs flock by when MTV axquiz prog.",
      thumb: reqImages.classes,
    },
    {
      title: "multiple payments to choose",
      desc:
        "The quick brown fox jumps over a lazy dog. \
     DJs flock by when MTV axquiz prog.",
      thumb: reqImages.multipay,
    },
    {
      title: "flexible timing",
      desc:
        "The quick brown fox jumps over a lazy dog. \
     DJs flock by when MTV axquiz prog.",
      thumb: reqImages.flexible,
    },
  ];

const filteredBenefits = listReducer(joinCards, 3);

export { joinCards as allBenefits, filteredBenefits };
