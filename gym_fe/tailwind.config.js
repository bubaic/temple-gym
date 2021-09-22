module.exports = {
  purge: { content: ["./**/*.html", "./src/**/*.vue"] },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: "#ede9fe",
          primary: "#12c78f",
          secondary: "#57d0d1",
          greenAlt: "#1E8C0E",
          yellow: "#ffd200",
          lime: "#8fdb5e",
          ash: "#707070",
        },
      },
      fontFamily: {
        pt: "PT",
        poppins: "Poppins",
      },
      width: {
        46: "11.5rem",
        76: "19rem",
        "2xs": "300px",
        "12ch": "12ch",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
