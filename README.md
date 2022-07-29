# radish.ai
<b/>1.) Description</b><br />
<br />Radish.ai is a data driven crop recommendation system for sustainable agriculture.

<br />≿————-　❈　————-≾<br /><br />
<b/>2.) How it works</b><br />
<br />Radish.ai takes in, cleans up, and preprocesses datasets (Python) of historical temperatures and rainfall around the globe. When a user inputs their location into the IO interface (built with JS, CSS, HTML), ML regression models (Python) are run on the environmental features to gain insights into projected environmental conditions for the given location. Next, the projected conditions are put into a KNN algorithm (R) with a dataset of the optimal agricultural conditions of 20 practical crops to recommend the top crops of each month with growing conditions most similar to the projected environmental conditions of the location. These recommendations, along with further insights and information, are presented to the user on the Radish.ai web application.

<br />≿————-　❈　————-≾<br /><br />
<b/>3.) Datasets</b>
<br /><br />
Average temp - https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data<br />
Rainfall - https://www.kaggle.com/datasets/iamkevin/united-states-rainfall<br />
T20 crops - <br />

<br />≿————-　❈　————-≾<br /><br />
<b/>4.) Contributions</b>
<br /><br />
Front end prototype - Jonathan, Renee via Figma<br />
Web dev - Jonathan via WebFlow<br />
KNN recommendation - Julia<br />
ML regression - Alvin<br />
Coordinate matching + misc. - Julia<br />
Data visualization - Alvin<br />
Preprocessing - Alvin<br />
