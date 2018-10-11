/*
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
*/

package traits

/**
 * Methods to manage user credentials.
 */
trait Users {
  Map env = System.getenv()
  Map getUserOne() {
    [username:env['GWELLS_USERNAME'], password:env['GWELLS_PASSWORD']]
  }

  Map getViewerUser() {
    [username:env['GWELLS_VIEWER_USERNAME'], password:env['GWELLS_PASSWORD']]
  }

  Map getSubmissionUser() {
    [username:env['GWELLS_SUBMISSION_USERNAME'], password:env['GWELLS_PASSWORD']]
  }

  Map getRegistryUser() {
    [username:env['GWELLS_REGISTRY_USERNAME'], password:env['GWELLS_PASSWORD']]
  }
}