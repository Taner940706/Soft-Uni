import { html } from '../../node_modules/lit-html/lit-html.js';
import { getAllClears } from '../api/data.js';

const dashboardTamplate = (clear) => html`<section id="dashboard">
<h2>Job Offers</h2>
${clear.length == 0 ? html`<h2>No offers yet.</h2>` : clear.map(c => html`
<div class="offer">
  <img src="${c.imageUrl}" alt="${c.imageUrl}" />
  <p>
    <strong>Title: </strong
    ><span class="title">${c.title}</span>
  </p>
  <p><strong>Salary:</strong><span class="salary">${c.salary}</span></p>
  <a class="details-btn" href="/details/${c._id}">Details</a>
</div>`)}
</section>`;

export async function dashboardPage(ctx) {
    const clear = await getAllClears();
    console.log(clear);
    ctx.render(dashboardTamplate(clear));
}