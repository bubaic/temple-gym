import Icon from "./Icon";

Icon.register({
  facebook: {
    width: 20,
    height: 20,
    raw: `
    <g style="fill:none">
      <rect width="20" height="20"/>
      <rect style="fill:none" x="0.5" y="0.5" width="19" height="19"/>
    </g>
    <g transform="translate(5.833 1.667)">
      <path
        style="stroke:#fff;fill:none;stroke-linejoin:round;stroke-width:1.5px"
        d="M15,1.667H12.5A4.167,4.167,0,0,0,8.333,5.833v2.5h-2.5v3.334h2.5v6.666h3.334V11.667h2.5L15,8.333H11.667v-2.5A.833.833,0,0,1,12.5,5H15Z"
        transform="translate(-5.833 -1.667)"/>
    </g>`,
  },
});
