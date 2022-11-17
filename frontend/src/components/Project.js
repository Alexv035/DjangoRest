import React from 'react'

const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>
                {project.note}
            </td>
            <td>
                {project.date_creation}
            </td>
            <td>
                {project.date_update}
            </td>
            <td>
                {project.user}
            </td>
            <td>
                {project.actives}
            </td>
        </tr>
    )
}


const ProjectList = ({ projects }) => {
    return (
        <table>
            <th>
                Notes
            </th>
            <th>
                Date creation
            </th>
            <th>
                Date update
            </th>
            <th>
                User
            </th>
            <th>
                Active / Passive
            </th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList