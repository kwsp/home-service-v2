import axios from 'axios';

import apiBaseURL from './config';


function fetchHomeAPI(url) {
    axios.get(apiBaseURL + url)
        .then((res) => {
            return res.data;
    })
}

export { fetchHomeAPI };

