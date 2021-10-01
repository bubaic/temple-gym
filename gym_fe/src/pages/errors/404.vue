<template>
  <section class="section">
    <div class="row">
      <img :src="img404" alt="not found" />
      <div class="details">
        <h1>404</h1>
        <p>
          Sorry, but the page you're looking for can't be found or no longer
          exists. Please go back to <RouterLink to="/">homepage.</RouterLink>
        </p>
      </div>
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

    .details {
      @extend %flexRow;
      @apply items-center justify-center divide-x divide-warm-gray-300
        max-w-prose my-5;

      h1,
      p {
        @apply p-2;
      }

      h1 {
        @extend %errGradient;
        @apply text-3xl lg:text-4xl font-poppins
				font-bold leading-none;
      }

      p {
        @apply text-sm md:text-base leading-tight tracking-wider
				 text-blue-gray-500 font-pt <sm:w-60;
        font-family: "syne";

        a {
          @apply text-light-blue-600;
        }
      }
    }
  }
</style>
