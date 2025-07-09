document.addEventListener('DOMContentLoaded', function () {
    const internshipList = [
        {
            title: "Software Developer Intern",
            company: "TechCorp",
            duration: "3 months",
            location: "Remote"
        },
        {
            title: "Data Scientist Intern",
            company: "DataLab",
            duration: "6 months",
            location: "On-site"
        },
        {
            title: "UX/UI Designer Intern",
            company: "Design Studios",
            duration: "4 months",
            location: "Remote"
        }
    ];

    const internshipContainer = document.querySelector('.internship-list');
    internshipList.forEach(internship => {
        const card = document.createElement('div');
        card.classList.add('internship-card');
        card.innerHTML = `
            <h3>${internship.title}</h3>
            <p><strong>Company:</strong> ${internship.company}</p>
            <p><strong>Duration:</strong> ${internship.duration}</p>
            <p><strong>Location:</strong> ${internship.location}</p>
        `;
        internshipContainer.appendChild(card);
    });
});
