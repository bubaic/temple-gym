<template>
  <section class="section">
    <div class="row">
      <img :src="img404" alt="not found" />
      <h1>403</h1>
      <p>
        Forbidden! Your access to this page has no longer exists. Please go back
        to <RouterLink to="/">homepage.</RouterLink>
      </p>
    </div>
  </section>
</template>

<script>
  import NotFoundImage from "@/assets/img/notFound.webp";
  export default {
    setup: () => {
      return { img404: NotFoundImage };
    },
  };
</script>

<style lang="scss" scoped>
  @import "@/assets/styles/reusable";

  .section {
    @apply bg-brand h-full;
  }
  .row {
    @extend .contain, %flexColumn;
    @apply <sm:px-2 sm:px-4 py-10 h-screen;

    img {
      @apply w-auto h-1/2 object-cover rounded-sm shadow-md;
    }

    h1 {
      @extend %errGradient;
      @apply text-3xl md:text-4xl xl:text-5xl font-poppins
				font-bold mt-6 mb-2 leading-none;
    }

    p {
      @apply text-sm md:text-lg leading-snug tracking-wider
				text-center text-warm-gray-500 font-pt;

      a {
        @apply text-light-blue-600;
      }
    }
  }
</style>
