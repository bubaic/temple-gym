<template>
  <div class="navbar">
    <div class="logo">
      <!-- <img src="img/logo.png" class="w-10 flex-none" /> -->
      <strong class="capitalize ml-1 flex-1">temple gym</strong>

      <button id="sliderBtn" class="md:block w-6 h-6 relative">
        <!-- :class="{ opened: flowMenuOpened }"  -->
        <a class="hamburger"></a>
      </button>
    </div>

    <!-- navbar content -->
    <div id="navbar" class="navbar__content">
      <!-- left -->
      <div class="text-gray-600 md:w-full md:flex md:flex-row md:justify-evenly md:pb-10 md:mb-10 md:border-b md:border-gray-200">
        <a class="mr-2 transition duration-500 ease-in-out hover:text-gray-900" href="#" title="email"><i class="fad fa-envelope-open-text"></i></a>        
        <a class="mr-2 transition duration-500 ease-in-out hover:text-gray-900" href="#" title="email"><i class="fad fa-comments-alt"></i></a>        
        <a class="mr-2 transition duration-500 ease-in-out hover:text-gray-900" href="#" title="email"><i class="fad fa-check-circle"></i></a>        
        <a class="mr-2 transition duration-500 ease-in-out hover:text-gray-900" href="#" title="email"><i class="fad fa-calendar-exclamation"></i></a>        
      </div>
      <!-- end left -->
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/reusable";

.bg {
  background: #e6e8ee;
}

@layer base {
  .navbar {
    @extend %flexRow, .bg;
    @apply md:fixed md:w-full md:top-0 md:z-20 flex-wrap p-6;

    .logo {
      @extend %flexRow;
      @apply flex-none w-56;
    }

    &__content {
      @extend %flexRow;
      @apply animated md:fixed md:top-0 md:w-full md:left-0 
        md:mt-16 md:border-t md:p-10 flex-1 md:bg-white
        flex-wrap justify-between md:flex-col pl-3
        // md:hidden;
    }
  }

  .hamburger {
    @apply w-6 h-1 rounded-md block
        cursor-pointer relative bg-brand-yellow;

    &::before,
    &::after {
      content: "";
      @apply absolute w-8 h-1 rounded-md bg-brand-yellow
        outline-none left-0;
    }

    &::before {
      @apply -top-2;
    }
    &::after {
      @apply top-2;
    }
  }
}
</style>
