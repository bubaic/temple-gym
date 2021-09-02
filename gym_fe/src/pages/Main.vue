<template>
  <p>it works</p>

  <!-- <div>
    <HeroSection />
    <StorySection />
    <SectionJoin />
    <JoinNow />
    <Trainers />
    <SectionFooter />
  </div> -->
</template>

<script>
import HeroSection from "@/components/sections/SectionHero";
import StorySection from "@/components/sections/SectionStory";
import SectionJoin from "@/components/sections/SectionJoin";
import JoinNow from "@/components/sections/SectionJoinNow";
import Trainers from "@/components/sections/SectionTrainers";
import SectionFooter from "@/components/sections/SectionFooter";

export default {
  components: {
    HeroSection,
    StorySection,
    SectionJoin,
    Trainers,
    JoinNow,
    SectionFooter,
  },
};
</script>
