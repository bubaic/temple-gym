import { assets } from "@/assets/img";
import { listReducer } from "./filter";

const pgmImages = assets.devBG,
  gymPrograms = [
    {
      title: "nutrition counselling",
      desc: `
        Experts works with the individual to asses his/her usual dietary \
        intake & identify areas where change is needed.
      `,
      thumb: pgmImages.b2,
    },
    {
      title: "fitness assesment",
      desc: `
        We've set-up a dynamic exercise program after assessing your fitness \
        that based on your personal goals, metabolism, & fitness level.
      `,
      thumb: pgmImages.b1,
    },
    {
      title: "fat loss program",
      desc: `
        We're providing the best weight loss training(s) as fitness isn't \
        about burning calories alone. It's about building a healthy body & a
        healthy mind.
      `,
      thumb: pgmImages.b3,
    },
    {
      title: "personal training",
      desc: `
        Do you need help hitting your fitness goals? Our team of personal \
        trainers will help you get in the shape you desire with proper training.
      `,
      thumb: pgmImages.b4,
    },
  ],
  filteredPrograms = listReducer(gymPrograms, 3);

export { gymPrograms as allPrograms, filteredPrograms };
