<template>
  <!-- timeline -->
  <div id="about">
    <section class="company">
      <!-- header -->
      <header class="header">
        <!-- <img :src="headerImg.img" :alt="headerImg.alt" /> -->
        <h1>
          <span>about us</span>
          <div></div>
        </h1>
      </header>

      <!-- company story -->
      <div class="company__story">
        <div class="wrapper">
          <div class="txt">
            <h2 class="headtitle">how it all started...</h2>
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Corporis
              similique consequatur neque, deleniti quod ullam voluptates?<br /><br />

              Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque
              voluptates dolore officiis odio maiores ea animi veritatis illum.
              Aliquid eius praesentium doloribus velit nisi assumenda quasi qui
              mollitia perferendis temporibus?
            </p>
          </div>
          <div class="img">
            <!-- <img :src="usrImg" :alt="usrImg.alt" /> -->
          </div>
        </div>
      </div>

      <!-- timeline -->
      <div class="company__timeline">
        <h2 class="headtitle">roadmap</h2>
        <!-- <Timeline /> -->
      </div>

      <!-- our teams -->
      <div class="company__team">
        <div class="team-highlight"></div>
        <h2 class="headtitle">meet the team!</h2>
        <Teams />
      </div>

      <div class="company__vision">
        <div class="wrapper">
          <div class="img">
            <!-- <img :src="visImg.img" :alt="visImg.alt" /> -->
          </div>
          <div class="txt">
            <h2 class="headtitle">vision</h2>
            <p>
              Lorem ipsum dolor sit, amet consectetur adipisicing elit.
              Veritatis commodi error possimus dolor nam unde, cum odio vitae,
              debitis sapiente minus ratione esse molestiae quae libero dolore
              labore laboriosam laborum.
            </p>
          </div>
        </div>
      </div>

      <div class="company__mission">
        <div class="wrapper">
          <div class="txt">
            <h2 class="headtitle">mission</h2>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Asperiores pariatur itaque quae molestias, perspiciatis ea
              temporibus beatae natus nostrum, dolorum, tenetur libero impedit
              corrupti. Magni saepe recusandae voluptatem exercitationem ullam?
            </p>
          </div>
          <div class="img">
            <!-- <img :src="misImg.img" :alt="misImg.alt" /> -->
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Teams from "@/layouts/team/Teams.vue";
// import Timeline from "@/layouts/Timeline";
// import { assets } from "@/assets/img/index";

export default {
  components: { Teams /* Timeline */ },
  setup: () => {
    // const headerImg = assets.devBG.b5,
    //   usrImg = assets.devDumpedImage.u1,
    //   visImg = assets.devBackIllustrations.vision,
    //   misImg = assets.devBackIllustrations.mission;
    // return { headerImg, usrImg, misImg, visImg };
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/_reusable.scss";

.blurry {
  background: rgba(0, 0, 0, 0.075);
}
@supports (
  (-webkit-backdrop-filter: blur(2em)) or (backdrop-filter: blur(2em))
) {
  .blurry {
    background: #000000cc;
    backdrop-filter: blur(2em) opacity(0.25);
    -webkit-backdrop-filter: blur(2em) opacity(0.25);
  }
}

@layer base {
  %common {
    @extend .atMobile, .contain;
    @apply my-16;

    p {
      @apply sm:mx-auto;
    }
  }
}

@layer base {
  #about {
    @apply h-full overflow-x-hidden;
  }

  .headtitle {
    @apply text-gray-600 w-max font-poppins font-bold \
      capitalize text-xl sm:mx-auto sm:text-2xl;
  }
  .header {
    @apply px-4 py-20 relative;

    h1 {
      @extend %flexRow;
      @apply z-10 relative justify-center;

      span {
        @apply text-xl sm:text-2xl xl:text-4xl font-poppins \
          text-brand capitalize font-bold w-auto z-10;
      }

      div {
        @extend .blurry;
        @apply w-44 h-10 absolute inline-block \
          left-1/2 transform -translate-x-1/2;
      }
    }

    img {
      @apply w-full h-full absolute top-0 left-0 \
        object-cover;
    }
  }
  .img {
    @extend %flexRow;
    @apply sm:justify-center;

    img {
      @apply rounded-full w-40 h-auto shadow-md;
    }
  }

  .txt {
    p {
      @apply mt-6 font-pt text-gray-500 leading-snug;
      max-width: 60ch;

      &::first-letter {
        @apply font-bold text-4xl pr-0.5;
      }
    }
  }

  .company {
    &__mission,
    &__vision,
    &__story,
    &__team {
      @extend %common;

      .wrapper {
        @extend %flexRow;
        @apply flex-wrap sm:flex-nowrap gap-4;

        & > .txt,
        & > .img {
          @apply w-full sm:w-1/2;
        }
      }
    }

    &__timeline {
      @extend .atMobile;
    }

    &__team {
      @apply pb-4 pt-8;

      .team-highlight {
        @apply absolute bg-brand-primary -left-1/4 -right-1/4 \
          top-0 bottom-0;
      }
    }

    &__team,
    &__timeline {
      .headtitle {
        @apply mx-auto z-10 relative;
      }
    }

    &__mission,
    &__vision {
      img {
        @apply h-full w-3/4 sm:w-2/3 mx-auto sm:mx-0 rounded-none \
        shadow-none;
      }
    }
    &__vision {
      .wrapper {
        @apply flex-wrap-reverse sm:flex-nowrap;
      }
    }
  }
}
</style>
